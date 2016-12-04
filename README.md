# How to represent sets and access Twitter's API with Python
## October 25, 2015

I followed much of the <a href="https://en.wikipedia.org/wiki/Canadian_federal_election,_2015">Canadian election</a> over <a href="https://twitter.com/">Twitter</a> because I live in Seattle. This got me wondering whether there is a large overlap in Twitter followers between the party leaders or if people just follow a single party.

The day after the election I used Tweepy to collect a list of follower IDs from @JustinTrudeau, @pmharper, @ThomasMulcair, @ElizabethMay, and @GillesDuceppe.

Sets are typically represented with Venn diagrams. The first option I came across was Ben Frederickson’s <a href="https://github.com/benfred/venn.js">code</a> for producing proportional Venn diagrams with D3. The result is really great! Unfortunately, it’s not really possible to represent five proportional overlapping sets with circles. You can see that overlaps between Duceppe, Mulcair, and May were excluded from this representation.

<i>Click this image to see interactive tooltip</i>

All possible intersections can be represented with elliptical Venn diagrams. I produced this plot with the <a href="https://cran.r-project.org/web/packages/VennDiagram/">VennDiagram</a> package in <a href="https://cran.r-project.org/">R</a>. But the ellipses are not proportional.

<img src="https://hmvantol.github.io/venn-followers/venn_followers_R.svg">

Ultimately, I like <a href="http://circos.ca/">this</a> chord diagram the best. This visualization was translated into D3 by <a href="http://bl.ocks.org/mbostock/4062006">Mike Bostock</a>. While it doesn’t show all possible set intersections, it is easy to read and you can get a sense of the overlap between each leader’s followers. People do, however, get counted multiple times in this diagram if they are following more than two party leaders.

<i>Click this image to open graphic</i>

Mulcair has a lot less followers than I expected considering he was the leader of the opposition for four years. Harper and Trudeau’s followers have remarkably similar affiliations with a large chunk that follow only Harper and/or Trudeau.

<br>
<b>Source material:</b>
<br><a href="http://www.tweepy.org/">Tweepy</a>
<br><a href="http://www.benfrederickson.com/venn-diagrams-with-d3.js/">Venn Diagrams with D3.js</a> by Ben Frederickson
<br><a href="https://cran.r-project.org/web/packages/VennDiagram/VennDiagram.pdf">draw.quintuple.venn {VennDiagram}</a>
<br><a href="http://bl.ocks.org/mbostock/4062006">Chord Diagram</a> by Mike Bostock
