# e621-json-dump
JSON Dumping Scripts for e621's API.
<hr>

<code>main.py</code> Scrapes https://e621.net/posts.json. Scrapes as much as it can (~950,000 Posts). Saves to JSON file. Takes ~6 hours to complete.<br>
<code>tag_export.py</code> Exports tag data from the huge JSON file to a smaller file for easier interpretation.<br>
<code>tag_count.py</code> Counts tag data from the exported JSON file. (Artist, General, Species, Characters, etc.)<br>
<code>id_export.py</code> Exports all post ids from the huge JSON file to a smaller file for easier interpretation.<br>
<code>id_count.py</code> Counts all ids from the exported JSON file. Gives total number of posts.<br>
<code>date_export.py</code> Exports all dates from huge JSON file to a smaller file for eaasier interpretation.<br>
<code>date_count</code> Plots date data from exported JSON file.
