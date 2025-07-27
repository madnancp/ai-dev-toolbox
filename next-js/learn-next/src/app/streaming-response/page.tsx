"use client"
import { Button } from "@/components/ui/button";
import { getStreamingResponse } from "@/services/streaming.service";
import { ChevronLeftIcon, Loader } from "lucide-react";
import Link from "next/link";
import { useEffect, useState } from "react";

const StreamingResponse = () => {
  const [data, setData] = useState<string>("")
  const [isStart, setIsStart] = useState<boolean>(false)

  useEffect(() => {
    if (!isStart) return;

    const cleanup = getStreamingResponse((chunk) => {
      setData((prev) => prev + " " + chunk);
    });

    return () => {
      cleanup();
    };

  }, [isStart]);

  return (
    <div className="flex items-center justify-center">
      <Button className="fixed top-3 left-5">
        <Link href={"/"} className="flex items-center gap-2">
          <ChevronLeftIcon />
          Home
        </Link>
      </Button>

      <div className="my-30 max-w-3/4">
        <Button variant={"outline"} onClick={() => { setIsStart(true) }}>
          Start Stream
          {isStart && (
            <Loader className="animate-spin" />
          )}
        </Button>

        {isStart && (
          <div className="min-w-3/4 mt-5">
            {data}
          </div>
        )}
      </div>
    </div>
  )
}

export default StreamingResponse;
