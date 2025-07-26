export default function Home() {
  return (
    <div className="flex justify-center items-center h-screen">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start bg-gray-800 p-5 rounded-lg">
        <ol className="flex flex-col">
          <a href="/section-1" className="hover:text-blue-300 hover:underline">1. Practice Questions</a>
          <a href="/section-2" className="hover:text-blue-300 hover:underline">2. Practical Quesions.</a>
          <a href="/todo" className="hover:text-blue-300 hover:underline">3. TODO app.</a>
          <a href="/streaming-response" className="hover:text-blue-300 hover:underline">4. Streaming Response</a>
        </ol>
      </main>
    </div>
  );
}
