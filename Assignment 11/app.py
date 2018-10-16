from flask import Flask, jsonify
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
import datetime as dt
Base = automap_base()
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/api/v1.0/precipitation")
def prcp():
	trip_start_date = dt.date(2015, 10, 17)
	year_back = trip_start_date - dt.timedelta(days = 365)
	session= Session(engine)
	results = session.query(Measurement.date, Measurement.prcp).filter(func.strftime("%Y %m %d",Measurement.date)<= trip_start_date).filter(func.strftime("%Y %m %d", Measurement.date)> year_back).all()
	result_list=[]
	for res in results:
		result_list.append({"Date": res.date,"Prcp": res.prcp})
	return (jsonify(result_list))


@app.route("/api/v1.0/stations")
def stations():
	session=Session(engine)
	results = session.query(Station.id, Station.station).all()
	station_list = []
	for res in results:
		station_list.append({"Station id": res.id, "Station name": res.station})
	return (jsonify(station_list))


@app.route("/api/v1.0/tobs")
def tobs():
	trip_start_date = dt.date(2015, 10, 17)
	year_back = trip_start_date - dt.timedelta(days = 365)
	session= Session(engine)
	results = session.query(Measurement.date, Measurement.tobs).filter(func.strftime("%Y %m %d",Measurement.date)<= trip_start_date).filter(func.strftime("%Y %m %d", Measurement.date)> year_back).all()
	result_list=[]
	for res in results:
		result_list.append({"Date": res.date,"Temp": res.tobs})
	return (jsonify(result_list))

@app.route("/api/v1.0/<start>/<end>")
def start_date(start, end):
	session=Session(engine)
	results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(func.strftime("%Y %m %d",Measurement.date)>= start).filter(func.strftime("%Y %m %d",Measurement.date)<= end)
	return(jsonify(results[0]))


if __name__ =="__main__":
	app.run(debug=True)
