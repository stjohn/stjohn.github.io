/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             TextInputStream.java
** CHANGES:
   28 Oct 1997       Java 1.1 can't handle '\r' in DOS files--sheesh, that 
                     used to work fine in 1.0
****************************************************************************/

/**
 * An input stream that can read numbers
 * @version 1.00 11 Apr 1997
 * @author Cay Horstmann
 */

package ccj;
import java.io.*;

public class TextInputStream extends InputStream
{  /**
    * Reads a line from the stream
    * @return the line, without the terminating newline. If a blank line is read, the empty string is returned.
    * If the end of input has been reached an no character has been
    * read, the empty string is returned and the stream is set to a failed state.
    */

   public String readLine()
   {  flushTiedStream();
      if (failFlag) return "";
      int ch;
      String r = "";
      boolean done = false;
      while (!done)
      {  ch = read();
         if (ch < 0)
         {  done = true;
            if (r.length() == 0) failFlag = true;
         }
         else if ((char)ch == '\r')
         {  done = true;
            ch = read();
            if (ch != '\n') unread(ch);
         }
         else if ((char)ch == '\n')
            done = true;
         else
            r = r + (char) ch;
      }
      return r;
   }

   private void flushTiedStream()
   {  if (out != null) try { out.flush(); } catch(IOException e) {}
   }

   private void skipSpace()
   {  if (failFlag) return;
      int ch;
      for(;;)
      {  ch = read();
         if (ch < 0)
         {  failFlag = true;
            return;
         }
         else if (!java.lang.Character.isSpace((char)ch))
         {  unread(ch);
            return;
         }
      }
   }

   /**
    * Reads a word from the stream. A word is a string delimited by white space.
    * @return the line, without the surrounding white space. 
    * If the end of input has been reached an no character has been
    * read, the empty string is returned and the stream is set to a failed state.
    */

   public String readWord()
   {  flushTiedStream();
      skipSpace();
      if (failFlag) return "";
      int ch;
      String r = "";
      boolean done = false;
      while (!done)
      {  ch = read();
         if (ch < 0)
            done = true;
         else if (java.lang.Character.isSpace((char)ch))
         {  done = true;
            unread(ch);
         }
         else
            r = r + (char) ch;
      }
      return r;
   }

   /**
    * Reads the next character from the stream. 
    * @return the character, as a one-character string. 
    * If the end of input has been reached an no character has been
    * read, the empty string is returned and the stream is set to a failed state.
    */

   public String readChar()
   {  flushTiedStream();
      if (failFlag) return "";
      int ch;
      String r = "";
      ch = read();
      if (ch >= 0)
         r = r + (char)ch;
      else
         failFlag = true;
      return r;
   }

   private String readDigits()
   {  String r = "";
      if (failFlag) return r;
      for(;;)
      {  int ch = read();
         if (ch < 0) return r;
         else if (!java.lang.Character.isDigit((char)ch))
         {  unread(ch);
            return r;
         }
         else
            r = r + (char) ch;
      }
   }

   /**
    * Reads an integer (in decimal) from the stream. 
    * @return the integer value. 
    * If the input is not a valid integer, the number zero is returned and the stream is set to a failed state.
    */

   public int readInt()
   {  flushTiedStream();
      skipSpace();
      if (failFlag) return 0;
      int ch;
      String r = "";
      boolean done = false;
      boolean digits = false;
      ch = read();
      if (ch == '+' || ch == '-')
         r = r + (char)ch;
      else if (ch < 0)
      {  done = true;
         failFlag = true;
      }
      else unread(ch);
      r += readDigits();
      if (failFlag) return 0;
      try
      {  return Integer.valueOf(r).intValue();
      } catch(NumberFormatException e)
      {  failFlag = true;
         return 0;
      }
   }

   /**
    * Reads a floating-point number from the stream. 
    * @return the floating-point value. 
    * If the input is not a valid floating-point number, the number zero is returned and the stream is set to a failed state.
    */

   public double readDouble()
   {  flushTiedStream();
      skipSpace();
      if (failFlag) return 0;
      int ch;
      String r = "";
      boolean done = false;
      boolean digits = false;
      ch = read();
      if (ch == '+' || ch == '-')
         r = r + (char)ch;
      else if (ch < 0)
         failFlag = true;
      else unread(ch);
      r += readDigits();
      ch = read();
      if (ch == '.')
      {  r = r + (char)ch;
         r += readDigits();
      }            
      else if (ch >= 0) unread(ch);
      ch = read();
      if (ch == 'E' || ch == 'e')
      {  r = r + (char)ch;
         ch = read();
         if (ch == '+' || ch == '-')
            r = r + (char)ch;
         else if (ch >= 0) unread(ch);
         r += readDigits();
      }
      else if (ch >= 0) unread(ch);
      if (failFlag) return 0;
      try
      {  return Double.valueOf(r).doubleValue();
      } catch(NumberFormatException e)
      {  failFlag = true;
         return 0;
      }
   }

   /**
    * Constructs a text input stream that reads its input from a file 
    * @param s the file name
    */

   public TextInputStream(String s)
   {  try
      {  in = new PushbackInputStream(new FileInputStream(s));
         out = null;
         failFlag = false;
         eofFlag = false;
      }
      catch (IOException e)
      {  in = null;
         out = null;
         failFlag = true;
         eofFlag = true;
      }  
   }

   TextInputStream(InputStream s)
   {    in = new PushbackInputStream(s);
        out = null;
        failFlag = false;
        eofFlag = false;
   }


   TextInputStream(InputStream s, OutputStream tied)
   {    in = new PushbackInputStream(s);
        out = tied;
        failFlag = false;
        eofFlag = false;
   }

   /**
    * Tests if the output stream is no longer valid
    * @return <tt>true</tt> if the stream has failed
    */

   public boolean fail() { return failFlag; }

   /**
    * Reads one character from the input stream.
    * @return the character read, or -1 at the end of input.
    * 
    */

   public int read() 
   {  if (failFlag || eofFlag) return -1;
      try
      {  int ch = in.read();
         if (ch == -1) eofFlag = true;
         return ch;
      }
      catch (IOException e)
      {  failFlag = true;
         return -1;
      }
   }

   /**
    * Returns one character to the input stream, to be read again
    * @param x the character to be pushed back
    */

   public void unread(int x)
   {  try
      {  in.unread(x);
      } catch(IOException e)
      {  failFlag = true;
      }
   }

   /**
    * Closes the input stream
    */

   public void close()
   {  try
      {  in.close();
      }
      catch(IOException e)
      {  failFlag = true;
      }
   }

   private PushbackInputStream in;
   private OutputStream out;
   private boolean failFlag;
   private boolean eofFlag;
}

