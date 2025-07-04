import { Button } from "@/components/ui/button";
import { useState } from "react";

const ThemeSwitcher = () => {
  const [change, setChange] = useState<boolean>(false);
  return (
    <div className={`${change ? 'bg-black' : 'bg-white'} flex justify-center items-center gap-2 flex-col border rounded-3xl shadow`
    }>

      <Button onClick={() => { setChange(!change) }}>{!change ? 'Change to Black' : 'change back!'}</Button>

    </div >


  )
}

export default ThemeSwitcher;
