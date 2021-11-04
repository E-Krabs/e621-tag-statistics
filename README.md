# e621-json-dump
Scripts to analyze the furry fandom through the content it produces and consumes.

"Images are posted to e621 all the time! There are lots of them there, and more every day. This gives us quite a bit of data, but one of the benefits of the site is the rather stringent dedication to tagging that it has: every image must be tagged with information describing what's in it, who's in it, who created it, and so on. In addition to tagging, e621 lets you favorite and rate posts. Using these two bits of data, we can estimate how popular something is in furry media in terms of both creating and consumption." - explore621<br>


<hr>

<ul>
  <li><code>main.py</code> Dumps https://e621.net/posts.json. Dumps as much as it can (~950,000/~2.5mil Posts). Takes ~6 hours to complete.<br>
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
  <li><strike><b>Extract</b> <code>created_at</code> and <code>tags</code> to plot popularity of a tag over a time period.</strike></li>
  <b>[++++++++++] 100%</b><br>
  <li><b>Merge</b> <code>tag_export.py</code> and <code>tag_count.py</code>.</li>
  <b>[++________] 20%</b>
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
