import {
  BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer
} from "recharts";

export default function Dashboard({ results }) {
  const data = results.map((r, i) => ({
    name: `C${i + 1}`,
    score: r.final_score,
  }));

  return (
    <div className="card">
      <h2>📊 Candidate Scores</h2>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="score" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}