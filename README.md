# e621-json-dump
<h3><b>About</b></h3>
Scripts to analyze the furry fandom through the content it produces and consumes.<br>

Every image on e621 must be tagged with info describing what's in it (characters, artist, acts, etc.). Using this information provided via the <a href="https://e621.net/posts.json">e621 API</a>, we can plot the popularity of something in furry media.

<h3><b>Fetching Data</b></h3>
This project fetches data from e621 provided via the <a href="https://e621.net/posts.json">e621 API</a>. <code>main.py</code> collects as much data as it can. This opperation can take a few hours, because API requests are limited to 2 per second. But we make requests only once per second to avoid a 503 (too many requests). Every request returns 320 posts. The script writes the returned results to a JSON file (~4.5GB) for later analysis.

<hr>
<ul>
  <li><code>main.py</code> Dumps https://e621.net/posts.json. Dumps as much as it can (~3,001,695 posts). Takes ~5.2 hours to complete.<br>

  <li><code>tag_export.py</code> Exports tag data from the huge JSON file to a smaller file for easier interpretation.<br></li>
  <li><code>tag_count.py</code> Plots tag data. (Artist, General, Species, Characters, etc.)<br></li>
  <li><code>tag_popularity.py</code> Plots the popularity of two tags over a period of time.<br></li>
  <li>Rest of .py's just compare tags over a period of time. Results are in <code>/Reports</code></li>
</ul>

<h3><b>Requirements:</b></h3>
<ul>
  <li>matplotlib</li>
  <li>pandas</li>
  <li>requests</li>
  <li>bigjson (if Memory < 64GB)</li>
</ul>

<h3><b>Memory:</b></h3>
<b>Required:</b> > 32GB<br>
There's a lot of information that gets writen (~4.5GB). <code>json.load()</code> loads the entire .json file into memory. Use <code>bigjson</code> in <code>tag_export.py</code> if your RAM < 64GB (You could squeeze the file into 32GB if you close all other applications). If your RAM < 32, ignore <code>tag_export.py</code> and use <code>bigjson</code> for everything. I've heard of <code>ijson</code> but havn't given it a try.

<h3><b>TODO:</b></h3>
<ul>
  <li>Optimize <code>main.py</code>, so it won't take a day long to fetch. I think it's <code>json.dumps()</code></li>
  <li>Find source of random 501s in <code>main.py</code></li>
  <li>✓ <strike>Extract< <code>created_at</code> and <code>tags</code> to plot popularity of a tag over a time period.</strike></li>
  <b>[++++++++++] 100%</b><br></li>
  <li>✓ <strike>Create admin dashboard</strike></li>
  <li>✓ <strike>omit_empty - Omit entries with value of 0.</strike></li>
  <li>omit_final - Omit the final entry (which might skew the line low when run during the begining of the month).</li>
  <li>More attrative plots.</li>
  <li>Implement argparse</li>
</ul>
<br>
Expaned upon "<a href="https://explore621.net">explore621</a>" by <a href="https://adjectivespecies.com/">[adjective][species]</a> licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA</a>. Project source is licensed under the <a href="https://github.com/E-Krabs/e621-json-dump/blob/main/LICENSE">MIT License</a>
