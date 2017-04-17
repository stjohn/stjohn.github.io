<?php
if ($_POST) {
	$firstname = $_POST["firstname"];
	$lastname = $_POST["lastname"];
	$bread = $_POST["bread"];
	$cookingInst = $_POST["cookingInst"];
	$filling = $_POST["filling"];
	$comments= $_POST["comments"];
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">

<html> 
<head> 
<meta name="robots" content="noindex,  nofollow">
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>228 Sandwich Shop</title> 
<style type="text/css">
img {
	float: left;
	margin-right: 20px;
}
div {
	padding-top: 10px;
}
h1 {
	font-height: 200%;
	color: blue;
	border-bottom: 1px dotted blue;
}
</style>
</head>
<body>

<h1>
228 Sandwich Shop
</h1>

<div>
<p>
Thanks, <strong><?php print($firstname); print(" "); print($lastname); ?></strong>,
for your order!  Your sandwich will be ready shortly!
</p>
<br />
<ul>
	<li> Bread: <?php print($bread); print(" ("); print($cookingInst); print(")");?>
	<li> Filling: <?php print($filling);?>
	<li> Extras: <?php
if(isset($_POST['extras']))
{
   $extras = $_POST['extras'];
   $n        = count($extras);
   $i        = 0;

	echo "<ul>\n";
   while ($i < $n)
   {
      echo "<li>{$extras[$i]}\t \n";
      $i++;
   }
   echo "</ul>\n";
}
?>
	<li> Special Instructions: <?php print($comments); print("\n");  ?>
</ul>
</div>


</body> 
</html>


<?php

}

?>
