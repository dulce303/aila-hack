/*global fetch */

//https://6ya2yxpzskdzadctuyijz6ggwa0iqfje.lambda-url.us-west-2.on.aws/

export const handler = async (event) => {
  // TODO implement
  let response = {
    statusCode: 200,
    body: JSON.stringify('Hello from Lambda!'),
  };
  console.log(event);

  let data = "tell me about food";
  // Variables
  const baseUrl = "https://api.twelvelabs.io/v1.2";
  const apiKey = "";




  if (event.request === "gist") {
    if (event.trailername === "garfield") {

      data = {
        "video_id": "666581dbd22b3a3c97bf1d57",
        "types": [
          "title",
          "hashtag",
          "topic"
        ]
      };
    }
    data = {
      "video_id": "666581dbd22b3a3c97bf1d57",
      "types": [
        "title",
        "hashtag",
        "topic"
      ]
    };
    response = await fetch(baseUrl + "/gist", {
      method: "POST",
      headers: { "x-api-key": apiKey, "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
  }
  else if (event.request === "summary") {
    // SUMMARY REQUESTED
    data = {
      "video_id": "666581dbd22b3a3c97bf1d57",
      "type": "summary"
    };
    if (event.trailername === "garfield") {
      data = {
        "video_id": "666581dbd22b3a3c97bf1d57",
        "type": "summary"
      };
      response = await fetch(baseUrl + "/summarize", {
        method: "POST",
        headers: { "x-api-key": apiKey, "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });
    }
    response = await fetch(baseUrl + "/summarize", {
      method: "POST",
      headers: { "x-api-key": apiKey, "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

  }
  else if (event.request === "chapters") {
    data = {
      "video_id": "666581dbd22b3a3c97bf1d57",
      "type": "chapter"
    };

    if (event.trailername === "garfield") {
      data = {
        "video_id": "666581dbd22b3a3c97bf1d57",
        "type": "chapter"
      };
      response = await fetch(baseUrl + "/summarize", {
        method: "POST",
        headers: { "x-api-key": apiKey, "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });
    }
    response = await fetch(baseUrl + "/summarize", {
      method: "POST",
      headers: { "x-api-key": apiKey, "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
  }
  else if (event.request === "highlights") {
    data = {
      "video_id": "666581dbd22b3a3c97bf1d57",
      "type": "highlight",
      "prompt": "tell me about food\n"
    };

    if (event.trailername === "garfield") {
      data = {
        "video_id": "666581dbd22b3a3c97bf1d57",
        "type": "highlight",
        "prompt": "tell me about food\n"
      };
      response = await fetch(baseUrl + "/summarize", {
        method: "POST",
        headers: { "x-api-key": apiKey, "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });
    }
    response = await fetch(baseUrl + "/summarize", {
      method: "POST",
      headers: { "x-api-key": apiKey, "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
  }




  // Send request
  const json = await response.json();
  console.log(json);
  return json;
};
