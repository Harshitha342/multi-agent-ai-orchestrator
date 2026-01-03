import React, { useState } from "react";
import axios from "axios";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const runTask = async () => {
    setLoading(true);
    setResult(null);
    setError(null);

    try {
      const response = await axios.get("http://127.0.0.1:8000/run");
      setResult(response.data);
    } catch (err) {
      setError("Failed to run task. Is backend running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Multi-Agent AI Orchestrator</h1>

      <button onClick={runTask} disabled={loading}>
        {loading ? "Running..." : "Run Task"}
      </button>

      {error && (
        <p style={{ color: "red", marginTop: "20px" }}>{error}</p>
      )}

      {result && (
        <>
          <h2 style={{ marginTop: "30px" }}>Final Result</h2>
          <pre
            style={{
              background: "#f4f4f4",
              padding: "15px",
              borderRadius: "6px",
              overflowX: "auto",
            }}
          >
            {JSON.stringify(result, null, 2)}
          </pre>
        </>
      )}
    </div>
  );
}
