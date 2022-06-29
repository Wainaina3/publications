from crypt import methods
from flask import jsonify, request
from mainapp.counties import counties_bp
from mainapp.counties.counties import Counties, CountiesSchema



#insert one country into db
@counties_bp.route("/addCounty", methods=['POST']) 
def addCounty():
    name = request.json['name']
    population = request.json['population']
    governor = request.json['governor']
    countyhq = request.json['countyhq']

    county_data = {"name":name, "population":population, "governor":governor, "countyhq":countyhq}

    countiesSchema = CountiesSchema()
    #validate user data
    validated_county_data = Counties(**countiesSchema.load(county_data))

    newCountyId = validated_county_data.insert()

    return jsonify({"newcounty":"inserted new county"})

@counties_bp.route('/getAllCounties')
def getAllCounties():
    counties_schema = CountiesSchema()

    counties = Counties.get_all()

    counties_data = []

    for county in counties:
        counties_data.append(counties_schema.dump(county))

    return jsonify({"counties": counties_data})

@counties_bp.route('/sayhello')
def hellothere():
    return jsonify({'greetings':"Hello there"})


