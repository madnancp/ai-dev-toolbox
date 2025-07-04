"use client"
import Counter from "./components/Counter";
import CharCounterForm from "./components/forms/CharCounter";
import FeedBackForm from "./components/forms/FeedBack";
import JokeFetcher from "./components/JokeFecther";
import Like from "./components/Like";
import LiveClock from "./components/LiveClock";
import ThemeSwitcher from "./components/ThemeSwitcher";
import Toggler from "./components/Toggler";

const SectionTwo = () => {

  return (
    <div className="h-auto">
      <div className="h-screen mb-20">
        <h1 className="font-bold text-3xl text-center">Learn useState</h1>
        <div className="grid grid-cols-2 gap-3 h-full">
          <Counter />
          <Toggler />
          <Like />
          <ThemeSwitcher />
        </div>
      </div>

      <div className="h-80 mb-20">
        <h1 className="font-bold text-3xl text-center">Learn useEffect</h1>
        <div className="grid grid-cols-2 gap-3 h-full">
          <JokeFetcher />
          <LiveClock />
        </div>
      </div>

      <div className="h-80 mb-20">
        <h1 className="font-bold text-3xl text-center">Learn Form Handling</h1>
        <div className="grid grid-cols-2 gap-3 h-full">
          <FeedBackForm />
          <CharCounterForm />
        </div>
      </div>

    </div>
  )
}

export default SectionTwo;
