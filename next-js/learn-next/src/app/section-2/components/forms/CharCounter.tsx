import { Textarea } from "@/components/ui/textarea";
import { useState } from "react";

const CharCounterForm = () => {
  const [counter, setCounter] = useState<number>(0)
  const [message, setMessage] = useState<string>("")


  return (
    <form className="flex justify-center items-center gap-2 flex-col border rounded-3xl shadow" >
      <h1 className="text-lg font-bold">Type Something..</h1>
      <div>
        <Textarea
          placeholder="Type your message here."
          value={message}
          onChange={(e) => { setMessage(e.target.value); setCounter(e.target.value.length) }}
        />
      </div>

      <div>
        <span className="text-lg font-bolg">Character length: {counter}</span>
      </div>
    </form >
  )
}

export default CharCounterForm;
