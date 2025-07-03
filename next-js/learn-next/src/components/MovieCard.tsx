import { TMovie } from "@/types/shared";


const MovieCard = (props: TMovie) => {
	return (
		<div className="bg-gray-800 p-5 rounded-lg shadow-gray-200 m-4">
			<div className="flex flex-col ml-5 w-full items-start justify-center">
				<h2 className="font-bold text-3xl">{props.name}</h2>
				<span className="text-md text-gray-300">{props.director}</span>
				<span className="text-md text-orange-400">{props.genre}</span>
			</div>
		</div>
	)
}

export default MovieCard;
