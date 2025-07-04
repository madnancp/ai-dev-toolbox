import { Button } from "@/components/ui/button";
import { useState } from "react";

const Like = () => {
  const [isLike, setIsLike] = useState<boolean | null>(null);

  return (

    <div className="flex justify-center items-center gap-2 flex-col border rounded-3xl shadow">
      <span className={isLike ? `text-green-600` : `text-red-600`}>{isLike ? 'Oh You like this!' : isLike === null ? '' : 'Why you dont like this masterpieace.. have you seen this?'}</span>
      <img
        src="https://m.media-amazon.com/images/M/MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWY3XkEyXkFqcGc@._V1_.jpg"
        width={200}
        height={80}
        alt="intestellar"
      />

      <div className="flex gap-4">
        <Button variant="outline" size="sm" className="bg-green-600 text-white hover:bg-green-700 hover:text-white" onClick={() => setIsLike(true)}>Like</Button>
        <Button variant="destructive" size="sm" onClick={() => setIsLike(false)}>Dislike</Button>
      </div>
    </div >

  )

}

export default Like;
