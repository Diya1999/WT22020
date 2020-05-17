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
    name: "Predict",
    id: "0e41a996-3fe5-4d3f-8616-a0a798f8e5d0",
    method: "POST",
    address: "http://127.0.0.1:5000/predict",
    data:
      '{"id":"1", "gender": "Male", "age": "21", "hypertension": "False", "heart_disease": "True", "ever_married": "True", "work_type": "Private", "Residence_type": "Urban", "avg_glucose_level": "123", "bmi": "345", "smoking_status": "never_smoked"}',
    headers: {
      "Content-Type": "application/json"
    }
  });

  postman[Request]({
    name: "Metrics",
    id: "45c17282-40f6-42bc-bb20-fb4033d93767",
    method: "GET",
    address: "http://127.0.0.1:5000/metrics"
  });

  postman[Request]({
    name: "Correlation",
    id: "66968d9f-2ed9-461c-a7fb-3bf20380c692",
    method: "GET",
    address: "http://127.0.0.1:5000/correlation"
  });

  postman[Request]({
    name: "Confusion",
    id: "31042071-f4d6-45a0-b000-2cd1cfb40e4b",
    method: "GET",
    address: "http://127.0.0.1:5000/confusion"
  });
}
