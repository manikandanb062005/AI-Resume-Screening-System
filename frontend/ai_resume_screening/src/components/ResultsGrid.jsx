export default function ResultsGrid({ results }) {
  return (
    <div className="grid">
      {results.map((r, i) => (
        <div
          className={`card ${i === 0 ? "top" : ""}`}
          key={i}
        >
          {/* Rank */}
          <h3>🏆 Rank #{r.rank || i + 1}</h3>

          {/* Score */}
          <p><strong>Score:</strong> {r.final_score}%</p>

          <div className="bar-bg">
            <div
              className="bar-fill"
              style={{
                width: `${r.final_score}%`,
                background: "#4f46e5"
              }}
            />
          </div>

          {/* Status */}
          <p>
            <strong>Status:</strong>{" "}
            <span
              style={{
                fontWeight: "bold",
                color:
                  r.status === "Selected"
                    ? "#22c55e"
                    : r.status === "Consider"
                    ? "#f59e0b"
                    : "#ef4444",
              }}
            >
              {r.status}
            </span>
          </p>

          {/* Role */}
          <p><strong>Role:</strong> {r.suggested_role}</p>

          {/* Experience */}
          <p><strong>Experience:</strong> {r.experience_years} years</p>

          {/* Matching Skills */}
          <div>
            <p>✅ Matching Skills:</p>
            <div>
              {r.matching_skills?.length > 0 ? (
                r.matching_skills.map((s, i) => (
                  <span key={i} className="tag">{s}</span>
                ))
              ) : (
                <p style={{ color: "#888" }}>No matching skills</p>
              )}
            </div>
          </div>

          {/* Missing Skills */}
          <div>
            <p>❌ Missing Skills:</p>
            <div>
              {r.missing_skills?.length > 0 ? (
                r.missing_skills.map((s, i) => (
                  <span key={i} className="tag missing">{s}</span>
                ))
              ) : (
                <p style={{ color: "#888" }}>No missing skills</p>
              )}
            </div>
          </div>

          {/* 🔥 BIAS SECTION */}
          <div style={{ marginTop: "10px" }}>
            <p>⚖️ Bias Check:</p>

            {r.bias?.bias_detected ? (
              <>
                <p style={{ color: "#ef4444", fontWeight: "bold" }}>
                  Bias Detected ❌
                </p>
                <div>
                  {r.bias.bias_words.map((word, i) => (
                    <span key={i} className="tag missing">
                      {word}
                    </span>
                  ))}
                </div>
              </>
            ) : (
              <p style={{ color: "#22c55e" }}>
                No Bias ✅
              </p>
            )}
          </div>

        </div>
      ))}
    </div>
  );
}