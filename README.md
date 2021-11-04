# e621-json-dump
<h3><b>About</b></h3>
Scripts to analyze the furry fandom through the content it produces and consumes.<br>

Every image on e621 must be tagged with info describing what's in it (characters, artist, acts, etc.). Using this information provided via the <a href="https://e621.net/posts.json">e621 API</a>, we can plot the popularity of something in furry media.

<h3><b>Fetching Data</b></h3>
This project fetches data from e621 provided via the <a href="https://e621.net/posts.json">e621 API</a>. <code>main.py</code> collects as much data as it can. This opperation can take a few hours, because API requests are limited to 2 per second. But we make requests only once per second to avoid a 503 (too many requests). Every request returns 1000 posts. The script writes the returned results to a JSON file (~2.5GB) for later analysis.

<hr>
<ul>
  <li><code>main.py</code> Dumps https://e621.net/posts.json. Dumps as much as it can. Takes ~6 hours to complete.<br>
  <li><code>tag_popularity.py</code> Plots the popularity of two tags to compare (from 2007-2021).<br>
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
  <li>✓ <strike><b>Extract</b> <code>created_at</code> and <code>tags</code> to plot popularity of a tag over a time period.</strike></li>
  <b>[++++++++++] 100%</b><br>
  <li><b>Merge</b> <code>tag_export.py</code> and <code>tag_count.py</code>.</li>
  <b>[++________] 20%</b>
  <li>Plot more data.</li>
  <li><b>Create</b> admin dashboard</li>
  <li><b>Seaborn</b> for more attrative plots.</li>
  <li><b>omit_empty</b> - whether or not to omit entries with value of 0.</li>
  <li><b>omit_final</b> - whether or not to omit the final entry (which might skew the line low when run during the begining of the month).</li>
  <li><b>Implement</b> argparse</li>
  <li><b>Colours:</b> https://matplotlib.org/stable/gallery/color/named_colors.html, http://colormind.io/, https://towardsdatascience.com/making-matplotlib-beautiful-by-default-d0d41e3534fd</li>
</ul>
<br>
Based <i>heavily</i> off of this project: https://explore621.net/
#	C5H8NO4Na
