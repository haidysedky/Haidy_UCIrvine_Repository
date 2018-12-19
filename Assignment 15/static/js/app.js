function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
    // Use d3 to select the panel with id of `#sample-metadata`
    var sampleMetadata = d3.select("#sample-metadata");

    // Use `.html("") to clear any existing metadata
    sampleMetadata.html("");
    sampleMetadata.append("ul");

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    var selectedSample = d3.select("#selDataset").property("value");
    var url = "/metadata/" + selectedSample ; 

    d3.json(url).then(function(sample) {

      Object.entries(sample).forEach(([key,value]) => sampleMetadata.append('li')
                      .attr('class', 'item')
                      .text(`${key}: ${value}`)
      )
    })

    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
}

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var selectedSample = d3.select("#selDataset").property("value");
  var url = "/samples/" + selectedSample;
  console.log(url);

  d3.json(url).then( function(sample) {

    var titleSample = d3.select("#selDataset").property("value")
    // @TODO: Build a Bubble Chart using the sample data
    var samplesBubble  = sample.sample_values;
    var otuidsBubble = sample.otu_ids;
    var otulabelsBubble = sample.otu_labels;

    dataBubble = [{
    type:"scatter",
    mode:"markers",
    x: otuidsBubble,
    y: samplesBubble,
    marker: {size:samplesBubble,
             color:otuidsBubble},
    text: otulabelsBubble
        }]

    layoutBubble = {title:`Bubble Chart for Sample ${titleSample}`,
                    xaxis: {title:"otu_ids"},
                    yaxis:{title:"samples"}
                  }

    Plotly.newPlot('bubble', dataBubble, layoutBubble);
    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
    
    var sortable = [];
    for(var data in sample){
      sortable.push([data, sample[data]])
    }

    sortable.sort(function(a, b) {
    return b[1] - a[1];
    })

    var sampleValues = sortable[2][1];
    var otuIds = sortable[0][1];

    var slicedSamples = sampleValues.slice(0,10);
    var slicedIds = otuIds.slice(0,10);
    console.log(slicedSamples);
    console.log(slicedIds);


    trace = {type: "pie",
             labels: slicedIds,
             values: slicedSamples
           }
             ;
    data = [trace];
    layout = {title:`Top 10 Samples for sample ${titleSample}`};

    Plotly.newPlot("pie", data, layout);
  })

}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
