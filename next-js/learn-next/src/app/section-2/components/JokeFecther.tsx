import { Button } from "@/components/ui/button"
import { useEffect, useState } from "react"

type Joke = {
  id: number
  type: string
  setup: string
  punchline: string
}

const JokeFetcher = () => {
  const [joke, setJoke] = useState<Joke | null>(null)
  const [count, setCounter] = useState<number>(0);

  useEffect(() => {
    const fetchJoke = async () => {
      const response = await fetch("http://www.official-joke-api.appspot.com/jokes/random", {
        method: "GET"
      })
      const data: Joke = await response.json()
      setJoke(data)
    }

    fetchJoke()
  }, [count])
  return (
    <div className="flex justify-center items-center gap-2 flex-col border rounded-3xl shadow">
      <h1 className="text-lg font-bold">Read a Joke</h1>
      {joke && (
        <p className="text-sm text-gray-400">
          {joke.setup}
          <span className="text-yellow-400">{joke.punchline}</span>
        </p>
      )}

      <Button variant="outline" onClick={() => { setCounter(count => count + 1) }}>New</Button>
    </div>
  )
}

export default JokeFetcher;
