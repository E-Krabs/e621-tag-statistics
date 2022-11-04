# e621 Tag Counter
<h3><b>About</b></h3>
<b>My first data-set thing, im gonna train something on the images...</b><br>
Also see: <a href="https://github.com/E-Krabs/rule34_json_dump">rule34 version</a>.<br><br>
Every image on e621 must be tagged with info describing what's in it (characters, artist, etc.). Using this information provided via the <a href="https://e621.net/posts.json">e621 API</a>, we can plot the popularity of something.

<h3><b>Fetching Data</b></h3>
<b>NOTE:</b> Fetching data via the API is now obsolete as daily exports are now available...<br>
Just download the csv file and place it in your default path folder.

<hr>
<ul>
  <li><code>fetchall.py</code> Dumps https://e621.net/posts.json. Dumps ~2.9mil posts to SQLite database. Takes ~7.8-~12 hours to complete.<br>
  <li><code>sqlite_count.py</code> Plots tag data (Artist, General, Species, Characters, etc.) from databsae.<br></li>
  <li><code>tag_count_per_month.py</code> Compare any number of tags by count over date, then plot.<br></li>
  <li><code>comic_count.py</code> Count all general tags in a comic pool by count, then plot.<br></li>
  <li>Everything in <code>/Prefab/</code> are the scripts used for the reports. Results are in <code>/Reports/</code></li>
</ul>

<h3><b>How To Use?</b></h3>
<ul>
  <li>Cd to the repo: <code>cd C:/Users/User/Downloads/e621-json-dump-main</code></li>
  <li>Install requirements: <code>pip install -r requirements.txt</code></li>
  <li>Generate database: <code>python3 fetchall.py</code> (This will take many hours. Tqdm will let you know with a progress bar.)</li>
  <li>Generate report: <code>python3 sqlite_count.py</code> (Should only take ~3min)</li>
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
  <li>I want to download everything, every picture and train a recognition algoritmn, or a new img generator based off of these. Just need to buy a more hdds.</li>
  <li>✓ <strike>Reach 5GB of data.</strike></li>
  <li>✓ <strike>Update all files to use the new sqlite database.</strike></li>
  <li>Finish <a href="https://github.com/E-Krabs/rule34_json_dump">rule34 version of this.</a></li>
  <li>✓ <strike>Optimize <code>fetchall.py</code>, so it won't take a day long to fetch.</strike></li>
  <li>✓ <strike>Find source of random 501s in <code>fetchall.py</code></strike>.</li>
  <li>✓ <strike>Extract <code>created_at</code> and <code>tags</code> to plot popularity of a tag over a time period.</strike></li>
  <li>✓ <strike>Create admin dashboard.</strike></li>
  <li>✓ <strike>omit_empty - Omit entries with value of 0.</strike></li>
  <li>✓ <strike>omit_final - Omit the final entry (which might skew the line low when run during the begining of the month).</strike></li>
  <li>✓ <strike>More attrative plots.</strike></li>
  <li>Upload database to home server.</li>
  <li>✓ <strike>Convert data-set to a db (json -> SQLite).</strike>.</li>
  <li>More Reports:</li>
    <ul>
      <li>Compare Zootopia's influence on furry population with [a][s]'s data.</li>
      <li>✓ <strike>How many liters/year based on <code>cum</code>? (Cum Counter TM)</strike></li>
      <li>✓ <strike>Species Explorer</strike></li>
      <li>✓ <strike>Jurassic Park Dino Dong.</strike></li>
      <li>Finish Species Explorer.</li>
      <li><a href="https://e-krabs.github.io/e621-json-dump/Report/4.htm">Report 4</a> needs to be updated.</li>
      <li>✓ <strike>Count general tags in a comic pool.</strike></li>
  <li>Upload copyright tags</li>
  </ul>
</ul>
<br>
Expaned upon "<a href="https://explore621.net">explore621</a>" by <a href="https://adjectivespecies.com/">[adjective][species]</a> licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA</a>. Project source is licensed under the <a href="https://github.com/E-Krabs/e621-json-dump/blob/main/LICENSE">MIT License</a>
