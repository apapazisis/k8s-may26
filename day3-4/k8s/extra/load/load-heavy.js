import http from "k6/http";
import { check } from "k6";

const BASE_URL = __ENV.BASE_URL || "http://127.0.0.1:8081";

// Aggressive load: 500 VUs, no sleep between requests
export const options = {
  scenarios: {
    spike: {
      executor: "constant-vus",
      vus: 500,
      duration: "3m",
    },
  },
  thresholds: {
    http_req_failed: ["rate<0.10"],
  },
};

export default function () {
  const res = http.get(`${BASE_URL}/`);
  check(res, { "status is 200": (r) => r.status === 200 });
}
