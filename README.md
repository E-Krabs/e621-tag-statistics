# e621 Tag Statistics
<h3><b>About</b></h3>
Statistics on tags on e621 via their daily dump csv. Plots data using matplotlib or Google Charts via a Flask app.<br>
Every image on e621 must be tagged with info describing what's in it (characters, artist, etc.). Using this information provided via the <a href="https://e621.net/posts.json">e621 API</a>, we can plot the popularity of something.<br>
<b>Also:</b> <a href="https://github.com/E-Krabs/rule34_json_dump">rule34 version</a>.
<hr>

<h3><b>File Description</b></h3>
<ul>
  <li><code>main.py</code> The main statistics program. Chang list of tags to track in the script via <code>tag_name</code><br></li>
  <li><code>downloader.py</code> Downloads <b>ALL</b> images with certain tags and tag exclusion; No multithreading (10K ~5hr).<br></li>
  <li><code>app.py</code> The Flask app Google Charts version of matplotlib. Does the same thing as <code>main.py</code><br></li>
  <li><code>app_init.py</code> Functions for the Flask app that does the counting. Change list of tags to track in the script via <code>tag_name</code><br></li>
  <li><code>templates/index.htm</code> The template page for the Flask app.<br></li>
  <li>Everything in <code>/[OLD]/</code> Older versions of these scripts that used SQLite and JSON, before CSV dumps.</li>
</ul>

<h3><b>How To Use</b></h3>
<ul>
  <li>Download the CSV dump from e621. Place it in this directory.</li>
  <li>Open a Command Prompt and cd to this directory.</li>
  <li>Install requirements via pip to a venv. <code>pip install -r requirements.txt</code></li>
  <b>For main.py & app.py:</b>
  <ul>
    <li>Change tags you want to track via <code>tag_name</code>.</li>
  </ul>
  <b>For downloader.py</b>
  <ul>
    <li>Change directory to download to via <code>dld</code>.</li>
    <li>Change tags to include via <code>include_tags</code>.</li>
    <li>Change tags to exclude via <code>exclude_tags</code>.</li>
  </ul>
  <li>Run the script.</li>
  <li>Profit?</li>
</ul>
  
<h3><b>Requirements</b></h3>
<ul>
  <li>Python311</li>
  <li>matplotlib</li>
  <li>pandas</li>
  <li>flask</li>
  <li>tqdm</li>
</ul>

<h3><b>TODO</b></h3>
<ul>
  <li>☑ Downloader based on tag inclusion/exclusion (No multithreading to not overwhelm server).
  <li>☑ Google Charts via Flask app</li>
  <li>☑ Use new CSV downloads.</li>
  <li>☑ I want to download everything, every picture. <strike>and train a recognition algoritmn, or a new img generator based off of these.</strike></li>
  <li>☑ Update all files to use the new sqlite database.</li>
  <li>⬜ Finish <a href="https://github.com/E-Krabs/rule34_json_dump">rule34 version of this.</a></li>
  <li>☑ Optimize <code>fetchall.py</code>, so it won't take a day long to fetch.</li>
  <li>☑ Find source of random 501s in <code>fetchall.py</code>.</li>
  <li>☑ Extract <code>created_at</code> and <code>tags</code> to plot popularity of a tag over a time period.</li>
  <li>☑ Create admin dashboard.</li>
  <li>☑ omit_empty - Omit entries with value of 0.</li>
  <li>☑ omit_final - Omit the final entry (which might skew the line low when run during the begining of the month).</li>
  <li>☑ More attrative plots.</li>
  <li>☑ Upload database to home server.</li>
  <li>☑ Convert data-set to a db (json -> SQLite)..</li>
  <li>More Reports:</li>
    <ul>
      <li>⬜ Compare Zootopia's influence on furry population with [a][s]'s data.</li>
      <li>☑ How many liters/year based on <code>cum</code>? (Cum Counter TM)</li>
      <li>☑ Species Explorer</li>
      <li>☑ Jurassic Park Dino Dong.</li>
      <li>⬜ Finish Species Explorer.</li>
      <li>☑ Count general tags in a comic pool.</li>
  </ul>
</ul>
<br>
Expaned upon "<a href="https://explore621.net">explore621</a>" by <a href="https://adjectivespecies.com/">[adjective][species]</a> licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA</a>. Project source is licensed under the <a href="https://github.com/E-Krabs/e621-json-dump/blob/main/LICENSE">MIT License</a>
