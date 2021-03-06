// Auto-generated by the Load Impact converter

import "./libs/shim/core.js";

export let options = {
  maxRedirects: 4,
  duration: "1m",
  vus: 200
};

const Request = Symbol.for("request");
postman[Symbol.for("initial")]({
  options
});

export default function() {
  postman[Request]({
    name: "metrics",
    id: "3f0b6406-5445-4582-8714-8e2e23c7fb0f",
    method: "GET",
    address: "http://127.0.0.1:5000/metrics",
    headers: {
      "Content-Type": "application/json"
    }
  });

  postman[Request]({
    name: "addData1",
    id: "74e19885-e9db-475c-b8dc-0f4d51d03ab2",
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
    id: "36ff56e1-9044-41d0-808b-4cadf01f46c7",
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
    id: "d2e9a61b-13e2-42c6-a1d4-ddc4f7723008",
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
    id: "301dd4da-f354-499e-87b3-439ad7840d4c",
    method: "POST",
    address: "http://127.0.0.1:5000/addData",
    data:
      '{"id":"34567", "gender": "Male", "age": "21", "hypertension": "False", "heart_disease": "True", "ever_married": "True", "work_type": "Private", "Residence_type": "Urban", "avg_glucose_level": "123", "bmi": "345", "smoking_status": "never_smoked", "stroke":"False"}',
    headers: {
      "Content-Type": "application/json"
    }
  });
}
