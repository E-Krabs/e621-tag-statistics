# e621-json-dump
<h3><b>About</b></h3>
Scripts to analyze the furry fandom through the content it produces and consumes.<br>

Every image on e621 must be tagged with info describing what's in it (characters, artist, acts, etc.). Using this information provided via the <a href="https://e621.net/posts.json">e621 API</a>, we can plot the popularity of something in furry media.

<h3><b>Fetching Data</b></h3>
This project fetches data from e621 provided via the <a href="https://e621.net/posts.json">e621 API</a>. <code>main.py</code> collects as much data as it can. This opperation can take a few hours, because API requests are limited to 2 per second. But we make requests only once per second to avoid a 503 (too many requests). Every request returns 320 posts. The script writes the returned results to a JSON file (~4.5GB) for later analysis.

<hr>
<ul>
  <li><code>main.py</code> Dumps https://e621.net/posts.json. Dumps as much as it can. Takes ~24 hours to complete.<br>
  <li><code>tag_popularity.py</code> Plots the popularity of two tags to compare.<br>
  <li><b>Merge</b><code>tag_export.py</code> Exports tag data from the huge JSON file to a smaller file for easier interpretation.<br>
  <li><b>Merge</b><code>tag_count.py</code> Counts tag data from the exported JSON file. (Artist, General, Species, Characters, etc.)<br>
  <li><b>Merge</b><code>id_export.py</code> Exports all post ids from the huge JSON file to a smaller file for easier interpretation.<br>
  <li><b>Merge</b><code>id_count.py</code> Counts all ids from the exported JSON file. Gives total number of posts.<br>
</ul>

<h3><b>Requirements:</b></h3>
<ul>
  <li>matplotlib</li>
  <li>pandas</li>
  <li>requests</li>
</ul>

<h3><b>TODO:</b></h3>
<ul>
  <li><b>Optimize</b> <code>main.py</code>, so it won't take a day long to fetch.
  <li>✓ <strike><b>Extract</b> <code>created_at</code> and <code>tags</code> to plot popularity of a tag over a time period.</strike></li>
  <b>[++++++++++] 100%</b><br>
  <li>✓ <strike><b>Create</b> admin dashboard</strike></li>
  <li><b>Merge</b> <code>tag_export.py</code> and <code>tag_count.py</code>.</li>
  <li>✓ <strike><b>omit_empty</b> - whether or not to omit entries with value of 0.</strike></li>
  <li><b>omit_final</b> - whether or not to omit the final entry (which might skew the line low when run during the begining of the month).</li>
  <li><b>Seaborn</b> for more attrative plots.</li>
  <li><b>Implement</b> argparse</li>
</ul>
<br>
Expaned on "<a href="https://explore621.net">explore621</a>" by <a href="https://adjectivespecies.com/">[adjective][species]</a> licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA</a>. Project source is licensed under the <a href="https://github.com/E-Krabs/e621-json-dump/blob/main/LICENSE">MIT License</a>
