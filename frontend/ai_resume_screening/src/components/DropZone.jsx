import { useDropzone } from "react-dropzone";
import { UploadCloud } from "lucide-react";

export default function DropZone({ onFiles, label, multiple = false }) {
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop: (acceptedFiles) => onFiles(acceptedFiles),
    multiple,
  });

  return (
    <div
      {...getRootProps()}
      className={`border-2 border-dashed rounded-2xl p-6 text-center cursor-pointer transition
        ${isDragActive ? "bg-blue-500/20 border-blue-400" : "bg-white/10 border-gray-400"}
      `}
    >
      <input {...getInputProps()} />

      <UploadCloud className="mx-auto mb-3" size={40} />

      <p className="text-sm">
        {isDragActive
          ? "Drop files here..."
          : `Drag & drop ${label} or click`}
      </p>
    </div>
  );
}