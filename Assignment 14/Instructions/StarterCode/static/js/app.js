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

var date_input = d3.select("#datetime");
//console.log(date_input);
var date_inputed = date_input.text();

date_input.on ("change", function() {

	tableData.filter( tableData.date == date_inputed)
})
;