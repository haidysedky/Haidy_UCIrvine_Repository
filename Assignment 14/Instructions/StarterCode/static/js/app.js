// from data.js
var tableData = data;

// YOUR CODE HERE!
var ufo_table = d3.select("#ufo-table");

//console.log(ufo_table);

var table_body = ufo_table
				.append("tbody")

/*
	for (i=0 ; i < tableData.length; i++) {

	var table_row = table_body.append("tr")

	Object.entries(tableData[i]).forEach ( ([key, value]) => {
		//console.log(`key : ${key}, value : ${value}`);
		table_row.append("td").text(value)

	})
}
*/
tableData.forEach( function(data) {
	var table_row = table_body.append("tr")

	Object.entries(data).forEach(([key, value]) => {
		//console.log(`key : ${key}, value : ${value}`);
		table_row.append("td").text(value)

	})
});


//tableData.forEach(function(element, index) {
//	console.log(element.datetime)
//})
//;

var date_input = d3.select(".form-control");

date_input.on ("change", function() {

	d3.event.preventDefault();

//filter the dataset based on input from user

	var date_inputed = date_input.property("value");

	console.log(date_inputed);

	var tableFiltered = tableData.filter(data => data.datetime === date_inputed)

	//d3.event.preventDefault();
	
//delete the tables data
	//var table = document.getElementById("#ufo-table");
	//console.log(table)
	
	//for(var i = table.rows.length - 1; i > 0; i--)
	//{
    //table.deleteRow(i);
	//};
	table_body.html("");
	//d3.event.preventDefault();

//insert the tables filtered data
	table_body = d3.select("#ufo-table").append("tbody")

	tableFiltered.forEach( function(data) {
	var table_row = table_body.append("tr")

	Object.entries(data).forEach(([key, value]) => {
		//console.log(`key : ${key}, value : ${value}`);
		table_row.append("td").text(value)

	})
});
})
;


