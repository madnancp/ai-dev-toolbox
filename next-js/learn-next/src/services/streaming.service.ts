export const getStreamingResponse = (onChunk: (chunk: string) => void) => {
	const source = new EventSource(`${process.env.NEXT_PUBLIC_API_BASE_URL}/stream`);

	source.onmessage = (event) => {
		onChunk(event.data);
	};

	source.onerror = (err) => {
		console.error("Stream error:", err);
		source.close();
	};

	return () => {
		source.close(); // cleanup
	};
};
