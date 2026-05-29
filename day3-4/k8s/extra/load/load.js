import http from "k6/http";
import { check, sleep } from "k6";

const BASE_URL = __ENV.BASE_URL || "http://127.0.0.1:8081";

export const options = {
  stages: [
    { duration: "30s", target: 50 },   // ramp to 50 VUs
    { duration: "1m", target: 200 },   // ramp to 200 VUs
    { duration: "2m", target: 200 },   // hold 200 VUs
    { duration: "30s", target: 0 },    // ramp down
  ],
  thresholds: {
    http_req_failed: ["rate<0.05"],    // <5% failures
    http_req_duration: ["p(95)<2000"], // 95% under 2s
  },
};

export default function () {
  const res = http.get(`${BASE_URL}/`);
  check(res, {
    "status is 200": (r) => r.status === 200,
  });
  sleep(0.05);
}
