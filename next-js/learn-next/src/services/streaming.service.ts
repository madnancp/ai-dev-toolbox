export const getStreamingResponse = async (onChunk: (chunk: string) => void) => {
	const source = new EventSource(`${process.env.NEXT_PUBLIC_API_BASE_URL}/stream`);

	source.onmessage = (event) => {
		onChunk(event.data)
	}

	source.onerror = (err) => {
		source.close()
	}

	return () => {
		source.close()
	}


}
