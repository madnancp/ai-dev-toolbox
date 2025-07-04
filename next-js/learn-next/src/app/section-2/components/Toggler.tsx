import { Button } from "@/components/ui/button";
import { useState } from "react";

const Toggler = () => {
  const [showMore, setShowMore] = useState<boolean>(false)

  return (
    <div className="flex justify-center items-center gap-2 flex-col border rounded-3xl shadow">
      <h3 className="text-lg font-bold text-blue-400">TypeScript</h3>
      <Button variant="secondary" size="default" onClick={() => { setShowMore(!showMore) }}>
        {!showMore ? 'Click to know more!' : 'Hide'}
      </Button>

      {showMore &&
        <span className="text-sm text-gray-500 px-8">Typescript is develop and maintained by Microsoft. I love this language, because i love to working with typed langauges. Typescript is a superset of javascript, which means typescript have all feature that in javascript additionaly it have statical type.</span>
      }

    </div>
  )
}

export default Toggler;
