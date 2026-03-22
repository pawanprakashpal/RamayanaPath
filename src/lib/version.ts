import { cookies } from "next/headers";
import type { Version } from "@/types";
import { DEFAULT_VERSION, VERSION_COOKIE } from "./constants";

export async function getServerVersion(): Promise<Version> {
  const cookieStore = await cookies();
  const value = cookieStore.get(VERSION_COOKIE)?.value;
  if (value === "tulsidas" || value === "valmiki") return value;
  return DEFAULT_VERSION;
}
