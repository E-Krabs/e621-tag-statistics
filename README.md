# e621-json-dump
<h3><b>About</b></h3>
Scripts to analyze the furry fandom through the content it produces and consumes.<br>
Also see: <a href="https://github.com/E-Krabs/rule34_json_dump">rule34 version</a>.<br><br>
Every image on e621 must be tagged with info describing what's in it (characters, artist, acts, etc.). Using this information provided via the <a href="https://e621.net/posts.json">e621 API</a>, we can plot the popularity of something in furry media.

<h3><b>Fetching Data</b></h3>
This project fetches data from e621 provided via the <a href="https://e621.net/posts.json">e621 API</a>. <code>fetchall.py</code> collects about ~3mil posts. This opperation can take a few hours, because API requests are limited to 2 per second. But we make requests only once per second to avoid a 503 (too many requests). Every request returns 320 posts. The script writes the returned results to a SQLite database for later analysis.

<hr>
<ul>
  <li><code>fetchall.py</code> Dumps https://e621.net/posts.json. Dumps as much as it can (~2.9mil posts). Takes ~7.8-~12 hours to complete.<br>
  <li><code>json_to_sqlite.py</code> Converts our json file to a database for better access.</li>
  <li><code>sqlite_count.py</code> Plots tag data (Artist, General, Species, Characters, etc.).<br></li>
  <li><code>tag_count_per_month.py</code> Compare any number of tags by count over date, then plot.<br></li>
  <li><code>comic_count.py</code> Count all general tags in a comic pool by count, then plot.<br></li>
  <li>Everything in <code>/Prefab/</code> are the scripts used for the reports. Results are in <code>/Reports/</code></li>
</ul>

<h3><b>How To Use?</b></h3>
<ul>
  <li>Cd to the repo: <code>cd C:/Users/User/Downloads/e621-json-dump-main</code></li>
  <li>Install requirements: <code>pip install -r requirements.txt</code></li>
  <li>Generate data-set: <code>python3 fetchall.py</code> (This will take many hours. Tqdm will let you know with a progress bar.)</li>
  <li>Generate <code>report</code>: <code>python3 sqlite_count.py</code> (Should only take ~3min)</li>
  <li>profit?</li>
</ul>
  
<h3><b>Requirements:</b></h3>
<ul>
  <li>matplotlib==3.5.1</li>
  <li>pandas==1.3.5</li>
  <li>requests==2.26.0</li>
  <li>tqdm==4.62.3</li>
</ul>

<h3><b>TODO:</b></h3>
<ul>
  <li>✓ <strike>Reach 5GB of data!</strike></li>
  <li>✓ <strike>Update all files to use the new sqlite database.</strike></li>
  <li>Finish <a href="https://github.com/E-Krabs/rule34_json_dump">rule34 version of this.</a></li>
  <li>✓ <strike>Optimize <code>fetchall.py</code>, so it won't take a day long to fetch.</strike></li>
  <p>Searching through our seen list of md5s was what was slowing down. Changed to a dict.</p>
  <li>✓ <strike>Find source of random 501s in <code>fetchall.py</code></strike></li>
  <li>✓ <strike>Extract <code>created_at</code> and <code>tags</code> to plot popularity of a tag over a time period.</strike></li>
  <li>✓ <strike>Create admin dashboard</strike></li>
  <li>✓ <strike>omit_empty - Omit entries with value of 0.</strike></li>
  <li>✓ <strike>omit_final - Omit the final entry (which might skew the line low when run during the begining of the month).</strike></li>
  <li>✓ <strike>More attrative plots.</strike></li>
  <li>Upload data-set</li>
  <li>✓ <strike>Convert data-set to a db</strike></li>
  <li>More Reports:</li>
    <ul>
      <li>Compare Zootopia's influence on furry population with [a][s]'s data.
      <li>✓ <strike>How many liters/year based on <code>cum</code>? (Cum Counter TM)</strike></li>
      <li>✓ <strike>Species Explorer</strike></li>
      <li>✓ <strike>Jurassic Park Dino Dong</strike></li>
      <li>Finish Species Explorer</li>
      <li><a href="https://e-krabs.github.io/e621-json-dump/Report/4.htm">Report 4</a> needs to be updated.</li>
      <li>✓ <strike>Count general tags in a comic pool</strike></li>
  <li>Upload copyright tags</li>
  </ul>
</ul>
<br>
Expaned upon "<a href="https://explore621.net">explore621</a>" by <a href="https://adjectivespecies.com/">[adjective][species]</a> licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA</a>. Project source is licensed under the <a href="https://github.com/E-Krabs/e621-json-dump/blob/main/LICENSE">MIT License</a>
