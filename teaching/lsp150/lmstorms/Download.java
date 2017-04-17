import java.io.*;
import java.util.*;

import javax.comm.*;

public class Download {
  public static void main(String[] args) {
    String filename = args[args.length - 1];
    String portName = "COM1";
  
    for (int i = 0; i < args.length - 2; i++) {
      if (args[i].equals("-port")) portName = args[i + 1];
    }

    try { new Download(filename, portName); }
    catch (NoSuchPortException nspe) {
      System.out.println("Sorry, I don't know about the " +
          portName + " port.");
    }
    catch (PortInUseException piue) {
      System.out.println("Sorry, somebody else is using " +
          portName + ".");
    }
    catch (UnsupportedCommOperationException ucoe) {
      System.out.println(ucoe);
    }
    catch (IOException ioe) {
      System.out.println("An IOException occurred: " + ioe);
    }
  }
  
  private SerialPort mPort;
  private Reader mFileIn;
  private Writer mOut;
  private PortListener mPortListener;
  
  private static final int kCharSleep = 20;
  private static final int kTimeOut = 800;

  public Download(String filename, String portName)
      throws NoSuchPortException, PortInUseException,
      UnsupportedCommOperationException, IOException {
    initialize(portName);
    mFileIn = new FileReader(filename);
    run();
  }
    
  protected void initialize(String portName)
      throws NoSuchPortException, PortInUseException,
      UnsupportedCommOperationException, IOException {
    CommPortIdentifier id =
        CommPortIdentifier.getPortIdentifier(portName);
    mPort = (SerialPort)id.open("Download", 1000);
    mPort.setSerialPortParams(
        2400,
        SerialPort.DATABITS_8,
        SerialPort.STOPBITS_1,
        SerialPort.PARITY_NONE
    );
    Reader in = new InputStreamReader(mPort.getInputStream());
    mPortListener = new PortListener(in);
    mOut = new OutputStreamWriter(mPort.getOutputStream());
  }

  public void run() {
    int c, n = 1;
    try {
      sendReturn();
      sendReturn();
      while ((c = mFileIn.read()) != -1) {
        if (c == '\r') {
          sendReturn();
          if (mPortListener.isComplete() == false) {
            throw new DownloadException("Timed out waiting " +
                "for a response from the RCX.");
          }
          else if (mPortListener.isError() == true) {
            throw new DownloadException("Error: " + 
                mPortListener.getLastLine());
          }
          System.out.print(".");
          n++;
        }
        else if (c != '\n') {
          mPortListener.reset();
          mOut.write(c);
          mOut.flush();
          Thread.sleep(kCharSleep);
        }
      }
      sendReturn();
      sendReturn();
    }
    catch (InterruptedException ie) { System.out.println(ie); }
    catch (DownloadException de) {
      System.out.println();
      System.out.println("Line " + n + ":");
      System.out.println("  " + de.getMessage());
    }
    catch (IOException ioe) { System.out.println(ioe); }
    
    // Regardless of what happened, try to clean up.
    try {
      mPortListener.stop();
      mFileIn.close();
      mOut.close();
      mPort.close();
    }
    catch (IOException ioe) {}
    System.exit(0);
  }
  
  protected void sendReturn() throws IOException, InterruptedException {
    mOut.write('\r');
    mOut.flush();
    Thread.sleep(kCharSleep);
    // Wait for response, or time out.
    long savedTime = System.currentTimeMillis();
    boolean trucking = true;
    while (trucking) {
      if (mPortListener.isComplete()) trucking = false;
      long currentTime = System.currentTimeMillis();
      if (currentTime - savedTime > kTimeOut) trucking = false;
      Thread.sleep(20);
    }
  }
  
  public class PortListener
      implements Runnable {
    private Thread mThread;
    private BufferedReader mIn;
    private boolean mComplete = false;
    private boolean mError = false;
    private String mLastLine;

    public PortListener(Reader in) {
      mIn = new BufferedReader(in);
      mThread = new Thread(this);
      mThread.start();
    }

    public void run() {
      String line;
      try {
        while((line = mIn.readLine()) != null) {
          line = line.trim();
          mLastLine = line;
          if (line.indexOf("ok") != -1) mComplete = true;
          if (line.indexOf("redefine") != -1) mComplete = true;
          if (line.indexOf("undefined") != -1) mComplete = mError = true;
          if (line.length() == 0) mComplete = true;
        }
      }
      catch (IOException ioe) {
        System.out.println("PortListener: ioe " + ioe);
      }
    }
    
    public void stop() throws IOException {
      mThread.interrupt();
    }
    
    public void reset() { mComplete = false; mError = false; }
    public boolean isComplete() { return mComplete; }
    public boolean isError() { return mError; }
    public String getLastLine() { return mLastLine; }
  }
  
  public class DownloadException
      extends IOException {
    public DownloadException(String message) { super(message); }
  }
}