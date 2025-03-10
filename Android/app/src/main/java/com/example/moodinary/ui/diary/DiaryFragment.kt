package com.example.moodinary.ui.diary

import android.annotation.SuppressLint
import android.app.DatePickerDialog
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.content.ContextCompat
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.example.moodinary.R
import com.example.moodinary.databinding.FragmentDiaryBinding
import com.example.moodinary.ui.home.HomeFragmentDirections
import java.text.SimpleDateFormat
import java.util.Calendar
import java.util.Date
import java.util.Locale

class DiaryFragment : Fragment() {

    private var _binding : FragmentDiaryBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentDiaryBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        setLayout()
        dateFormat()
        datePicker()
        changedBtnColor()
    }

    private fun setLayout() {
        with(binding) {
            ivBack.setOnClickListener {
                findNavController().navigateUp()
            }
            tvSave.setOnClickListener {
                val action = DiaryFragmentDirections.actionDiaryToLoading()
                findNavController().navigate(action)
            }
        }
    }

    @SuppressLint("DefaultLocale")
    private fun datePicker() {
        binding.datePicker.setOnClickListener {
            val calendar = Calendar.getInstance()
            val year = calendar.get(Calendar.YEAR)
            val month = calendar.get(Calendar.MONTH)
            val day = calendar.get(Calendar.DAY_OF_MONTH)

            val datePickerDialog = DatePickerDialog(
                requireContext(),
                R.style.CustomDatePicker,
                { _, selectedYear, selectedMonth, selectedDay ->
                    val selectedDate = String.format("%d. %d. %d", selectedYear, selectedMonth + 1, selectedDay)
                    binding.datePicker.text = selectedDate
                },
                year,
                month,
                day
            )

            // 날짜 유효성 제한
            calendar.set(Calendar.YEAR, year)
            calendar.set(Calendar.MONTH, month)
            calendar.set(Calendar.DAY_OF_MONTH, day)
            datePickerDialog.datePicker.maxDate = calendar.timeInMillis

            datePickerDialog.show()
        }
    }

    private fun dateFormat() {
        val currentDate = Date()
        val dateFormat = SimpleDateFormat("yyyy.MM.dd", Locale.getDefault())
        val formattedDate = dateFormat.format(currentDate)
        binding.datePicker.text = formattedDate
    }

    private fun changedBtnColor() {
        binding.etWrite.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(
                charSequence: CharSequence?,
                start: Int,
                count: Int,
                after: Int
            ) {
                val color = ContextCompat.getColor(requireContext(), R.color.purple_60)
                binding.tvSave.setTextColor(color)
                // binding.btnWrite.setBackgroundResource(R.drawable.btn_write_selected)
            }

            override fun onTextChanged(
                charSequence: CharSequence?,
                start: Int,
                before: Int,
                after: Int
            ) {
                val color = ContextCompat.getColor(requireContext(), R.color.gray_20)
                binding.tvSave.setTextColor(color)
                // binding.btnWrite.setBackgroundResource(R.drawable.btn_write_unselected)
            }

            override fun afterTextChanged(editable: Editable?) {
                if ((editable?.length ?: 0) > 0) {
                    // 텍스트가 있을 때 버튼 색상 변경
                    val color = ContextCompat.getColor(requireContext(), R.color.purple_60)
                    binding.tvSave.setTextColor(color)
                    // binding.btnWrite.setBackgroundResource(R.drawable.btn_write_selected)
                } else {
                    // 텍스트가 없을 때 버튼 색상 원래대로
                    val color = ContextCompat.getColor(requireContext(), R.color.gray_20)
                    binding.tvSave.setTextColor(color)
                    // binding.btnWrite.setBackgroundResource(R.drawable.btn_write_unselected)
                }
            }
        })
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}