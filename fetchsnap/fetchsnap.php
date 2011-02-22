<?php

if (!isset ($_SERVER['argv'][1]))
    die ("Usage: {$_SERVER['argv'][0]} <url>" . PHP_EOL);

/**
 * Fetches the latest snapshot source package
 * @param string $url         url to snapshot src/
 * @param string $expression  xpath expression
 */
function xpath_url ($url, $expression)
{
    $data = file_get_contents ($url);

    $doc = new DomDocument ();
    $doc->loadHTML ($data);

    $sxe = simplexml_import_dom ($doc);
    $arr = $sxe->xpath ($expression);

    if (isset ($arr[0]))
        return (string) $arr[0];
  
    return null;        
}

$build_id = xpath_url ($_SERVER['argv'][1], "/html/body/table/tr[last()-1]/td/a");
$filename = xpath_url ($_SERVER['argv'][1] . "/{$build_id}", "/html/body/table/tr[last()-1]/td/a");

$snapshot_url = $_SERVER['argv'][1] . "/${build_id}/${filename}";
echo "The latest snapshot is {$snapshot_url}" . PHP_EOL;

exec ("wget $snapshot_url");
