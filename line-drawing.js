// From http://www.redblobgames.com/making-of/line-drawing/
// Copyright 2017 Red Blob Games <redblobgames@gmail.com>
// License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

const scale = 10;
let root = d3.select("#demo svg");
let A = { x: 0, y: 0 };
let B = { x: 0, y: 0 };

const drawGrid = () => {
  for (let x = 0; x < 50; x++) {
    for (let y = 0; y < 20; y++) {
      root
        .append("rect")
        .attr("transform", `translate(${x * scale}, ${y * scale})`)
        .attr("width", scale)
        .attr("height", scale)
        .attr("fill", "white")
        .attr("stroke", "gray");
    }
  }
};
drawGrid();

function highlightReact(A) {
  const { x, y, fill } = A;
  root
    .append("rect")
    .attr("transform", `translate(${x * scale}, ${y * scale})`)
    .attr("width", scale - 1)
    .attr("height", scale - 1)
    .attr("fill", fill);
}

function randomStartPoint() {
  const x = Math.floor(Math.random() * 10);
  const y = Math.floor(Math.random() * 10);
  return { x, y, fill: "hsl(0,40%,70%)" };
}

function randomEndPoint() {
  const x = Math.floor(Math.random() * 20) + 30;
  const y = Math.floor(Math.random() * 10);
  return { x, y, fill: "hsl(147, 50%, 47%)" };
}

function randomPoint() {
  drawGrid();
  const start = randomStartPoint();
  const end = randomEndPoint();
  A = start;
  B = end;
  highlightReact(start);
  highlightReact(end);
}

function findPath() {
  const body = {
    start: A,
    end: B,
  };
  fetch("http://localhost:8000/path", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  })
    .then((response) => response.json())
    .then((data) => {
      const points = data.data;
      points.forEach((element) => {
        const item = { ...element, fill: "hsl(192, 100%, 50%)" };
        highlightReact(item);
      });
    });
}
