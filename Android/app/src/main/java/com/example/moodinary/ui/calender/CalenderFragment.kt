package com.example.moodinary.ui.calender

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.example.moodinary.R
import com.example.moodinary.databinding.FragmentCalenderBinding
import com.example.moodinary.ui.home.HomeFragmentDirections
import com.prolificinteractive.materialcalendarview.CalendarDay
import com.prolificinteractive.materialcalendarview.format.ArrayWeekDayFormatter

class CalenderFragment : Fragment() {
    private var _binding : FragmentCalenderBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentCalenderBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        setLayout()
        setCalender()
    }

    private fun setLayout() {
        binding.btnTodayEmotion.setOnClickListener {
            val action = CalenderFragmentDirections.actionCalenderToReport()
            findNavController().navigate(action)
        }
    }

    private fun setCalender() {
        with(binding) {
            calender.selectedDate = CalendarDay.today()
            calender.setWeekDayFormatter(ArrayWeekDayFormatter(resources.getTextArray(R.array.custom_weekdays)))
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}