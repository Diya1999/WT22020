// Auto-generated by the Load Impact converter

import "./libs/shim/core.js";

export let options = {
  maxRedirects: 4,
  duration: "1m",
  vus: 100
};

const Request = Symbol.for("request");
postman[Symbol.for("initial")]({
  options
});

export default function() {
  postman[Request]({
    name: "metrics",
    id: "2bba4499-5661-4c36-8ec5-49fef4bc2b40",
    method: "GET",
    address: "http://127.0.0.1:5000/metrics",
    headers: {
      "Content-Type": "application/json"
    }
  });

  postman[Request]({
    name: "addData1",
    id: "1c9e8ea7-964e-4e54-8155-c70d6be11d28",
    method: "POST",
    address: "http://127.0.0.1:5000/addData",
    data:
      '{"id":"1", "gender": "Male", "age": "21", "hypertension": "False", "heart_disease": "True", "ever_married": "True", "work_type": "Private", "Residence_type": "Urban", "avg_glucose_level": "123", "bmi": "345", "smoking_status": "never_smoked", "stroke":"False"}',
    headers: {
      "Content-Type": "application/json"
    }
  });

  postman[Request]({
    name: "addData2",
    id: "f88e70f3-8e09-46a3-8057-cfe60cf039f5",
    method: "POST",
    address: "http://127.0.0.1:5000/addData",
    data:
      '{"id":"19876543", "gender": "Male", "age": "21", "hypertension": "False", "heart_disease": "True", "ever_married": "True", "work_type": "Private", "Residence_type": "Urban", "avg_glucose_level": "123", "bmi": "345", "smoking_status": "never_smoked", "stroke":"False"}',
    headers: {
      "Content-Type": "application/json"
    }
  });

  postman[Request]({
    name: "addData3",
    id: "adba0220-0960-4204-b780-db50f6ffc29c",
    method: "POST",
    address: "http://127.0.0.1:5000/addData",
    data:
      '{"id":" ", "gender": "Male", "age": "21", "hypertension": "False", "heart_disease": "True", "ever_married": "True", "work_type": "Private", "Residence_type": "Urban", "avg_glucose_level": "123", "bmi": "345", "smoking_status": "never_smoked", "stroke":"False"}',
    headers: {
      "Content-Type": "application/json"
    }
  });

  postman[Request]({
    name: "addData4",
    id: "63733efd-7a58-4cc0-961d-799a998bcff4",
    method: "POST",
    address: "http://127.0.0.1:5000/addData",
    data:
      '{"id":"34567", "gender": "Male", "age": "21", "hypertension": "False", "heart_disease": "True", "ever_married": "True", "work_type": "Private", "Residence_type": "Urban", "avg_glucose_level": "123", "bmi": "345", "smoking_status": "never_smoked", "stroke":"False"}',
    headers: {
      "Content-Type": "application/json"
    }
  });
}
