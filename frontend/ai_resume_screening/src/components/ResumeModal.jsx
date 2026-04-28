import { motion } from "framer-motion";


export default function ResumeModal({ resume, onClose }) {
  if (!resume) return null;

  return (
    <div className="fixed inset-0 bg-black/60 flex justify-center items-center z-50">
      <motion.div
        initial={{ scale: 0.8, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        className="bg-white text-black p-6 rounded-2xl w-[600px] max-h-[80vh] overflow-y-auto"
      >
        <h2 className="text-xl font-bold mb-4">Resume Preview</h2>

        <pre className="whitespace-pre-wrap text-sm">
          {resume.original_resume}
        </pre>

        <button
          onClick={onClose}
          className="mt-4 bg-red-500 text-white px-4 py-2 rounded"
        >
          Close
        </button>
      </motion.div>
    </div>
  );
}




