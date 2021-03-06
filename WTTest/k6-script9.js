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
    name: "getEntry1",
    id: "bf8ec3f7-f156-4bfe-9e26-7e602a91403e",
    method: "POST",
    address: "http://127.0.0.1:5000/getEntry/<id>",
    data: '{"id":"1"}',
    headers: {
      "Content-Type": "application/json"
    }
  });

  postman[Request]({
    name: "Delete1",
    id: "61edfd51-807b-408b-b850-bb3021ffed15",
    method: "DELETE",
    address: "http://127.0.0.1:5000/delEntry/1",
    headers: {
      "Content-Type": "application/json"
    }
  });

  postman[Request]({
    name: "getEntry2",
    id: "2d078c7e-9497-4f58-b280-40432f65a436",
    method: "POST",
    address: "http://127.0.0.1:5000/getEntry/<id>",
    data: '{"id":"123456789"}',
    headers: {
      "Content-Type": "application/json"
    }
  });

  postman[Request]({
    name: "getEntry3",
    id: "22df5384-dcb4-4674-a4a3-c4706e5c385e",
    method: "POST",
    address: "http://127.0.0.1:5000/getEntry/<id>",
    data: '{"id":"154"}',
    headers: {
      "Content-Type": "application/json"
    }
  });

  postman[Request]({
    name: "Delete2",
    id: "dcae3cb2-4039-43ec-96d5-fd63e10a4111",
    method: "DELETE",
    address: "http://127.0.0.1:5000/delEntry/1876543"
  });
}
