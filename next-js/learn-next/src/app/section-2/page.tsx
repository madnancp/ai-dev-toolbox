"use client"
import Counter from "./components/Counter";
import Like from "./components/Like";
import ThemeSwitcher from "./components/ThemeSwitcher";
import Toggler from "./components/Toggler";

const SectionTwo = () => {

  return (
    <div className="h-auto">
      <div className="h-screen">
        <h1 className="font-bold text-3xl text-center">Learn useState</h1>
        <div className="grid grid-cols-2 gap-3 h-full">
          <Counter />
          <Toggler />
          <Like />
          <ThemeSwitcher />
        </div>
      </div>
    </div>
  )
}

export default SectionTwo;
