# e621-json-dump
<h3><b>About</b></h3>
Scripts to analyze the furry fandom through the content it produces and consumes.<br>

Every image on e621 must be tagged with info describing what's in it (characters, artist, acts, etc.). Using this information provided via the <a href="https://e621.net/posts.json">e621 API</a>, we can plot the popularity of something in furry media.

<h3><b>Fetching Data</b></h3>
This project fetches data from e621 provided via the <a href="https://e621.net/posts.json">e621 API</a>. <code>fetchall.py</code> collects as much data as it can. This opperation can take a few hours, because API requests are limited to 2 per second. But we make requests only once per second to avoid a 503 (too many requests). Every request returns 320 posts. The script writes the returned results to a JSON file (~4.97GB) for later analysis.

<hr>
<ul>
  <li><code>fetchall.py</code> Dumps https://e621.net/posts.json. Dumps as much as it can (~2.5mil posts). Takes ~7.8-11.7 hours to complete.<br>
  <li><code>tag_export.py</code> Exports tag data from the huge JSON file to a smaller file for easier interpretation. (less memory intensive)<br></li>
  <li><code>tag_count.py</code> Plots tag data. (Artist, General, Species, Characters, etc.)<br></li>
  <li><code>/Runners/tag_count_per_month.py</code> Compare any number of tags in 'general' and 'species', then plot.<br></li>
  <li><code>/Runners/comic_count.py</code> Count all general tags in a comic pool, then plot.<br></li>
  <li>Everything in <code>/Prefab/</code> are the scripts used for the reports. Results are in <code>/Reports/</code></li>
</ul>

<h3><b>Requirements:</b></h3>
<ul>
  <li>matplotlib</li>
  <li>pandas</li>
  <li>requests</li>
</ul>

<h3><b>Memory:</b></h3>
<b>Required:</b> >= 32GB<br>
There's a lot of information that gets writen (~4.5GB). <code>json.load()</code> loads the entire .json file into memory. Converting to a db would probally be much better. Or maybe ijson. I havn't given these a try yet...

<h3><b>TODO:</b></h3>
<ul>
  <li>Finish <a href="https://github.com/E-Krabs/rule34_json_dump">rule34 version of this.</a></li>
  <li>✓ <strike>Optimize <code>fetchall.py</code>, so it won't take a day long to fetch.</strike></li>
  <p>Searching through our seen list of md5s was what was slowing down. Changed to a dict.</p>
  <li>Django app</li>
  <li>✓ <strike>Find source of random 501s in <code>fetchall.py</code></strike></li>
  <li>✓ <strike>Extract <code>created_at</code> and <code>tags</code> to plot popularity of a tag over a time period.</strike></li>
  <li>✓ <strike>Create admin dashboard</strike></li>
  <li>✓ <strike>omit_empty - Omit entries with value of 0.</strike></li>
  <li>✓ <strike>omit_final - Omit the final entry (which might skew the line low when run during the begining of the month).</strike></li>
  <li>✓ <strike>More attrative plots.</strike></li>
  <li>Upload data-set</li>
  <li>Convert data-set to a db</li>
  <li>More Reports:</li>
    <ul>
      <li>✓ <strike>How many liters/year based on <code>cum</code>? (Cum Counter TM)</strike></li>
      <li>✓ <strike>Species Explorer</strike></li>
      <li>✓ <strike>Jurassic Park Dino Dong</strike></li>
      <li>Finish Species Explorer</li>
      <li><a href="https://e-krabs.github.io/e621-json-dump/Report/4.htm">Report 4</a> needs to be updated.</li>
      <li>✓ <strike>Count general tags in a comic pool</strike></li>
      <li>That new Sing movie was shit, lets see how it did on e621</li>
  <li>Upload copyright tags</li>
  </ul>
</ul>
<br>
Expaned upon "<a href="https://explore621.net">explore621</a>" by <a href="https://adjectivespecies.com/">[adjective][species]</a> licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA</a>. Project source is licensed under the <a href="https://github.com/E-Krabs/e621-json-dump/blob/main/LICENSE">MIT License</a>
