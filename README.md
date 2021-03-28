# music-player
<br>
<h2>Overview</h2>
This is an audio player app where you can create and shuffle playlist.
<br><br>
<h2>Building the app</h2>
<h3>provided</h3>
<ul>
<li>music albums as a list of nested Python tuples and lists</li>
</ul>
<h3>requirements</h3>
<ul>
<li>user creates a playlist</li>
<li>shuffle feature</li>
<li>shuffled songs order must always be unique</li>
</ul>
<br><br>
<h2>Just a remark</h2>
„Shuffled songs order must always  be unique” requirement may be achieved by:
<ul>
<li>generating random songs order on user demand and memorizing it</li>
<li>calculate  all possible variations at once, memories them and provide the user one variation at a time</li>
</ul>
I went for the first solution in this case, although each of the two has it’s own props and cons.
