import { useState } from "react";
import UploadForm from "./components/UploadForm";
import ResultsGrid from "./components/ResultsGrid";
import Dashboard from "./components/Dashboard";
import Loader from "./components/Loader";

export default function App() {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);


  const handleDownload = async () => {
  try {
    const res = await fetch("http://localhost:8000/download-report", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(results),
    });

    const blob = await res.blob();

    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");

    a.href = url;
    a.download = "AI_Resume_Report.xlsx";
    a.click();

    window.URL.revokeObjectURL(url);
  } catch (err) {
    console.error(err);
    alert("Download failed!");
  }
};

  return (
    <div className="container">
      <h1>🚀 AI Resume Screening System</h1>

      <UploadForm
        setResults={setResults}
        setLoading={setLoading}
      />

      {loading && <Loader />}

      {!loading && results.length > 0 && (
        <>
          <Dashboard results={results} />
          <ResultsGrid results={results} />
          <button onClick={handleDownload} className="download-btn">
           📥 Download Excel Report
          </button>
        </>
      )}
    </div>
  );
}