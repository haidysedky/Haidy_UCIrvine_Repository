// @TODO: YOUR CODE HERE!
var svgWidth = 1000;
var svgHeight = 700;

var chartMargins = {top:20, bottom:20, right:20, left:20};

var chartWidth = svgWidth - chartMargins.left - chartMargins.right;
var chartHeight = svgHeight - chartMargins.top - chartMargins.bottom;

var svg = d3.select("#scatter").append("svg")
            .attr("width", svgWidth)
            .attr("height", svgHeight);

var chartGroup = svg.append("g")
	                  .attr("transform", `translate(${chartMargins.left}, ${chartMargins.top})`)

d3.csv("/assets/data/data.csv", function(Data){
	//if (error) return console.warn(error);

	Object.entries(Data).forEach(value => {
	  Data.poverty = +Data.poverty
	  Data.healthcare = +Data.healthcare
    console.log(Data.healthcare)
	});

  //Data.forEach(function(element){
    //Data.poverty = +Data.poverty
    //Data.healthcare = +Data.healthcare
  //})

	var xScale = d3.scaleLinear()
	               .domain(0,d3.max(Data, d => d.poverty))
	               .range(0,chartWidth);


	var yScale = d3.scaleLinear()
	               .domain(d3.extent(Data, d => d.healthcare)) 
	               .range(chartHeight,0);

	var bottomAxis = d3.axisBottom(xScale);
	      
  var leftAxis = d3.axisLeft(yScale);

  chartGroup.append("g")
            .attr("transform", `translate(0,${chartHeight})`)
            .call(bottomAxis)

  chartGroup.append("g")
            .call(leftAxis)

  chartGroup.selectAll("circle")
            .data(Data)
            .enter()
            .append("circle")
            .attr("cx", d => xScale(Data.poverty))
            .attr("cy", d => yScale(Data.healthcare))
            .attr("r",20)
            .attr("fill", "blue")
            .attr("opacity", ".5");

  var toolTip = d3.tip()
                  .attr("class", "d3-tip")
                  .offset([80, -60])
                  .html(function(d) {
                   return (`${d.abbr}`);
                  });
                  
  chartGroup.call(toolTip);

  chartGroup.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 0 - chartMargins.left)
            .attr("x", 0 - (chartHeight / 2))
            .attr("dy", "1em")
            //.classed("axis-text", true)
            .text("Lacks Healthcare (%)");

  chartGroup.append("text")
            //.attr("transform", "rotate(0)")
            .attr("y", 0 - chartMargins.bottom)
            .attr("x", 0 - (chartWidth / 2))
            .attr("dx", "1em")
            //.classed("axis-text", true)
            .text("In Poverty (%)");
})