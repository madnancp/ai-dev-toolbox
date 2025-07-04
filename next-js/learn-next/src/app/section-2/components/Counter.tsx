import { useState } from "react"
import { Button } from "@/components/ui/button";

const Counter = () => {
  const [count, setCount] = useState<number>(0);

  return (
    <div className="flex justify-center items-center gap-2 flex-col border rounded-3xl shadow">
      <h1 className="text-lg font-bold">Counter</h1>
      <div className="flex gap-5">
        <Button
          size="icon"
          onClick={() => { setCount(count => count - 1) }}
        >
          -
        </Button>
        <span className="text-lg font-bold">{count}</span>
        <Button
          size="icon"
          onClick={() => { setCount(count => count + 1) }}
        >
          +
        </Button>
      </div>
    </div>
  )
}

export default Counter;
