# EACOP_Path
Starting with background info:
The East African Crude Oil Pipeline (EACOP), also known as the Uganda-Tanzania Crude Oil Pipeline (UTCOP) is under construction and intended to transport crude oil from Uganda's oil fields to the Port of Tanga, Tanzania on the Indian Ocean. Once completed the pipeline will be the longest heated crude oil pieline in the world. <br>

As a part of the semester project, we were tasked that as if each of us is an engineer in the process engineering team dealing with pipeline design, where I and my teammate was the one being responsible for establishing optimum route by taking into following points: <br>
• To minimise the economic costs and environmental damage, the length of the pipeline has to be 
optimum (i.e., minimum). This can also be helpful in reducing the pressure drop. <br>
• No water resources (i.e., rivers, lakes), big cities, protected zones including national parks, zones 
where tunnel construction is needed (i.e., across the mountains), any war or guerrilla territories can be crossed. <br>

Did the following:
Coloring impassable areas first hypothetically and marking start and end points with a distinctive color for a better image recognition, a preliminary algorithm using Breadth-First Search was implemented without taking the precise locations of those areas as a starting step. <br>
However, then, with the selection of 20 pre-determined points that the path should pass through these points based on its surrounding environment, the method was facilitated further by sketching the line on Folium map, and the number of sample points was extended to 400 with shapely library. Those points were then used as input for gnuplot heatmap and Tableau wiz by retrieving the elevation value from Earth Engine API.

Visit [Tableau link](https://public.tableau.com/app/profile/akbar.bunyadzade/viz/ElevationProfileforEACOPproject/Sheet1)
