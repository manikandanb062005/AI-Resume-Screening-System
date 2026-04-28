import { useState } from "react";
import { analyzeFiles } from "../services/api";

export default function UploadForm({ setResults, setLoading }) {
  const [jdText, setJdText] = useState("");
  const [resumes, setResumes] = useState([]);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    if (resumes.length === 0) {
      return setError("Please upload at least one resume");
    }

    try {
      setLoading(true);
      setError("");

      const formData = new FormData();

      resumes.forEach((file) => formData.append("resumes", file));
      formData.append("job_description_text", jdText);

      const data = await analyzeFiles(formData);

      console.log("API RESPONSE:", data);

      // ✅ IMPORTANT FIX
      setResults(data.results);

    } catch (err) {
      console.error(err);
      setError("Something went wrong!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Upload Job Description & Resumes</h2>

      <textarea
        placeholder="Paste Job Description..."
        onChange={(e) => setJdText(e.target.value)}
      />

      <input
        type="file"
        multiple
        onChange={(e) => setResumes([...e.target.files])}
      />

      <button onClick={handleSubmit}>Analyze 🚀</button>

      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}