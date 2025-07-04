import { TProfile } from "@/types/shared";


const ProfileCard = (props: TProfile) => {
	return (
		<div className="bg-gray-800 p-5 rounded-lg shadow-gray-200 flex justify-between">
			<div>
				<img src={props.avatarUrl} alt={props.name} className="rounded-full shadow shadow-white" width={150} height={150} />
			</div>
			<div className="flex flex-col ml-5 w-full items-start justify-center">
				<h2 className="font-bold text-xl">{props.name}</h2>
				{
					props.isOnline ? <span className="text-green-400">online</span> : <span className="text-red-400">offline</span>
				}
				<span className="text-md text-gray-400">{props.bio ? props.bio : 'no bio'}</span>
			</div>
		</div>
	)
}

export default ProfileCard;
