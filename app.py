from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS=[
  {
    "id":1,
    "title":"Frontend Engineer",
    "location":"Jaipur,India",
    "salary":"Rs. 17,00,000"
  },
  
  {
    "id":2,
    "title":"Backend Engineer",
    "location":"Delhi,India",
    "salary":"Rs. 19,00,000"
  },
  
{
  "id":3,
  "title": "Software Engineer-SDE 1",
  "location": "Banglore,India",
  "salary": "Rs. 25,00,000"
},
  
{
  "id":4,
  "title": "Data Engineer ",
  "location":"Mumbai,India",
  "salary":"Rs. 19,00,000"
 }
]

@app.route("/")
def hello_jovian():
  return render_template("home.html", jobs=JOBS, company_name="Jovians Careers")

@app.route("/api/ jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
