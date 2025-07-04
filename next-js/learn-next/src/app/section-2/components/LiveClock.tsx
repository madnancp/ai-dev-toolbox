import { useEffect, useState } from "react";

const LiveClock = () => {
  const time = new Date();
  const [currTime, setCurrTime] = useState<Date>(new Date())

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrTime(new Date())
    }, 1000)
    return () => {
      clearInterval(interval)
    }
  }, []);

  const formatedTime = currTime.toLocaleTimeString()

  return (
    <div className="flex justify-center items-center gap-2 flex-col border rounded-3xl shadow">
      <h1 className="text-lg font-bold">Live Clock</h1>
      <span className="text-3xl font-bold">
        {formatedTime}
      </span>
    </div>
  )
}


export default LiveClock;
